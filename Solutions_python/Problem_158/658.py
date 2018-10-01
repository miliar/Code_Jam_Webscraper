'''
Created on 11.04.2015

@author: uscheller
'''
from copy import deepcopy
import sys

def to_field(omino):
    maxX = max([x for x, _ in omino]) + 1
    maxY = max([y for _, y in omino]) + 1
    l = [["." for _ in range(maxY)] for _ in range(maxX)]
    for x, y in omino:
        l[x][y] = "X"
    return l

def to_string(field):
    return "\n".join(["".join(x) for x in field]) + "\n"

def rotate(field):
    rotated = zip(*field[::-1])
    rotated = [[y for y in x] for x in rotated]
    return rotated

def mirrorY(field):
    return field[::-1]

def mirrorX(field):
    return [[y for y in reversed(x)] for x in field]

def fields_around(x, y):
    for a, b in ((1,0), (0,1), (-1,0), (0,-1)):
            yield x+a, y+b 

def normalize(omino):
    minX = min([x for x, _ in omino])
    minY = min([y for _, y in omino])
    return [(x-minX, y-minY) for x,y in omino]
    


class NOmino:
    def __init__(self, N):
        self.n = N
        self.ominoes = []
    
    def get_ominoes(self):
        if not self.ominoes:
            existing = set()
            for omino in self.generate():
                field = to_field(omino)
                if not to_string(field) in existing:
                    turn90 = rotate(field)
                    turn180 = rotate(turn90)
                    turn270 = rotate(turn180)
                    for x in field, turn90, turn180, turn270:
                        existing.add(to_string(x))
                        #existing.add(to_string(mirrorX(x)))
                        existing.add(to_string(mirrorY(x)))
                    self.ominoes.append(omino)
        return self.ominoes
    
    def generate(self):
        if self.n == 1:
            yield [(0,0)]
        else:
            ominoes = set()
            for omino in NOmino(self.n - 1).get_ominoes():
                omino_field_set = set(omino)
                for x, y in omino:
                    for a, b in fields_around(x, y):
                        if not (a,b) in omino_field_set:
                            new_omino = omino[:]
                            new_omino.append((a,b))
                            new_omino = normalize(new_omino)
                            new_omino_field = to_string(to_field(new_omino))
                            if not new_omino_field in ominoes:
                                ominoes.add(new_omino_field)
                                yield new_omino
    
        

def can_place(omino, field, x, y):
    next_field = deepcopy(field)
    for a, b in omino:
        if a+x < len(field) and b+y < len(field[0]) and next_field[a+x][b+y] == ".":
            next_field[a+x][b+y] = "X"
        else:
            return None
    return next_field


def solve_field(ominoes, field):
    empty_fields = any(["." in x for x in field])
    if not empty_fields:
        return True
    
    for _ in range(4):
        field = rotate(field)
        for field in (mirrorY(field), field):
            for x in range(len(field)):
                for y in range(len(field[0])):
                    if field[x][y] == ".":
                        for omino in ominoes:
                            next_field = can_place(omino, field, x, y)
                            if next_field:
                                result = solve_field(ominoes, next_field)
                                if result:
                                    return result
    
    return False

def can_gabriel_win(ominoes, field, richards_choice):
    for _ in range(2):
        field = rotate(field)
        for x in range(len(field)):
            for y in range(len(field[0])):
                next_field = can_place(richards_choice, field, x, y)
                if next_field and solve_field(ominoes, next_field):
                    return True
    return False

def can_richard_win(ominoes, field):
    for richards_choice in ominoes:
        if not can_gabriel_win(ominoes, field, richards_choice):
            return "RICHARD"
    return "GABRIEL"

def solve(X, R, C):
    field = [["." for _ in range(C)] for _ in range(R)]
    ominoes = NOmino(X).get_ominoes()
    return can_richard_win(ominoes, field)

def go_through(data):
    data = data[1:]
    s = ""
    for case, line in enumerate(data):
        X, R, C = [int(x) for x in line.split()]
        s += "Case #%d: %s\n" % (case + 1, solve(X, R, C))
    return s[:-1] # remove newline

if __name__ == '__main__':
    #for omino in NOmino(4).get_ominoes():
    #    print to_string(to_field(omino))
    print go_through(open(sys.argv[1]).readlines())
        
        