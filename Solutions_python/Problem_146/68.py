#!/usr/bin/python
import os, sys
exercise = os.path.split(__file__)[1][0] # A,B,C...
if len(sys.argv) > 1:
    variant = sys.argv[1] # sample, small-attempt0, ...
else:
    variant = raw_input('input variant: ')
input = '%s-%s.in' % (exercise,variant)
print 'reading input', input
input = file(input)
output = '%s-%s.out' % (exercise,variant)
print 'writing output', output
output = file(output,'w')

def reduce(n):
    if n >= 1000000007:
        n = n % 1000000007
    return n

def solve():
    N = int(input.readline())
    cars = input.readline().strip().split(' ')
    assert len(cars) == N

    LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    assert len(LETTERS) == 26

    for car in cars:
        for letter in car:
            assert letter in LETTERS, '%s not in %s (car=%s)' %(letter,LETTERS,car)

    print 'cars:', cars

    letters = [] # lettere trovate
    start_cars = {} # letter -> start cars
    end_cars = {} # letter -> end cars
    middle_cars = dict([(letter,0) for letter in LETTERS]) # letter -> count of cars
    middle_factorial = dict([(letter,1) for letter in LETTERS]) # letter -> count!
    next_cars = {} # letter -> letter
    prev_cars = {} # letter -> letter

    for letter in LETTERS:
        for car in cars:
            start = None
            end = None
            for (i,c) in enumerate(car):
                if c == letter:
                    if start is None:
                        start = i
                        end = i
                    if end != i:
                        print 'not connected %s: %s' % (letter,car)
                        return 0
                    end = i+1
            if start is not None:
                if not letter in letters:
                    letters.append(letter)
                if start>0:
                    # starting car for letter
                    if letter in start_cars:
                        print 'two starting cars for %s: %s and %s' % (letter,start_cars[letter],car)
                        return 0
                    start_cars[letter] = car
                if end<len(car):
                    # ending car for letter
                    if letter in end_cars:
                        print 'two ending cars for %s: %s and %s' % (letter,end_cars[letter],car)
                        return 0
                    end_cars[letter] = car

                if start>0:
                    c=car[start-1]
                    prev_cars[letter] = c
                    next_cars[c] = letter
                    print 'find connection %s -> %s (1)' % (c,letter)
                if end < len(car):
                    c=car[end]
                    prev_cars[c] = letter
                    next_cars[letter] = c
                    print 'find connection %s -> %s (2)' % (letter,c)

                if start == 0 and end == len(car):
                    # middle car
                    middle_cars[letter] += 1
                    middle_factorial[letter] *= middle_cars[letter]
                    middle_factorial[letter] = reduce(middle_factorial[letter])
        if letter in start_cars and letter in end_cars and start_cars[letter] == end_cars[letter] and middle_cars[letter]>0:
            print 'incompatible %s with middle cars' % start_cars[letter]
            return 0
    # completata struttura, ora cerco componenti connesse
    components = {}
    while letters:
        c = letters[0]
        cc = c
        # cerca la componente di c
        while c in prev_cars:
            c = prev_cars[c]
            if c == cc:
                print 'loop detected!'
                return 0
        component = c
        letters.remove(c)
        count = middle_factorial[c]
        while c in next_cars:
            c = next_cars[c]
            letters.remove(c)
            component += c
            count *= middle_factorial[c]
            count = reduce(count)
        components[component] = count
    product = 1
    factorial = 1
    for n,count in enumerate(components.values()):
        product *= count
        product = reduce(product)
        factorial *= n+1
    result = product * factorial
    result = reduce(result)
    return result

T = int(input.readline())
for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())
