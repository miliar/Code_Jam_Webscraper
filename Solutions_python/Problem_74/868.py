# To change this template, choose Tools | Templates
# and open the template in the editor.
import os

fn = 'E:\dev\GoogleJam\src\InOut\A-large'
try: os.remove(fn+'.out')
except: pass
fout = open(fn+'.out','w')
case = 0

class Robot:
    pos = 1
    free_move = 0
    def move_to(self, new_pos):
        time_needed = abs(self.pos - new_pos) + 1
        if self.free_move < time_needed:
            time_needed -= self.free_move
        else:
            time_needed = 1
        self.free_move = 0
        self.pos = new_pos
        return time_needed

def main():
    f = open(fn+'.in', 'r')
    global case
    for case in range(int(f.readline())):
        seq = f.readline().strip().split(' ')
        o = Robot()
        b = Robot()
        total_time = 0
        seq.pop(0)
        while seq:
            robot = seq.pop(0)
            new_pos = int(seq.pop(0))
            if robot == "B":
                t = b.move_to(new_pos)
                total_time += t
                o.free_move += t
                #print "B added", t
            else :
                t = o.move_to(new_pos)
                total_time += t
                b.free_move += t
                #print "O added", t

        put(total_time)

def put(res):
    print res
    fout.write("Case #" + str(case+1) + ": " + str(res) + "\n")


__author__="Louis"
__date__ ="$16 avr. 2011 10:41:32$"

if __name__ == "__main__":
    main()
