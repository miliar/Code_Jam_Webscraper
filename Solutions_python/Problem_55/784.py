# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="alvaro"
__date__ ="$May 7, 2010 8:13:08 PM$"

from collections import deque;

class Problem:
    def process_entry(self):
        sum = 0;
        print 'Case #%d:' % self.case,
        for i in range(self.R):
            occ = 0;
            for j in range(self.N):
                ondeque = int(self.queue.pop());
                self.queue.append(ondeque);
                if occ + ondeque > self.k:
                    break;
                self.queue.rotate();
                occ = occ + ondeque;
            sum = sum + occ;
        print sum;

    def read_entry(self):
        if self.next < len(self.input):
            self.case = self.case + 1;
            self.entry = self.next;
            data = self.input[self.entry].split();
            self.R = int(data[0]); #times in a day
            self.k = int(data[1]); #capacity of the coaster
            self.N = int(data[2]); # number of groups: len(groups)
            groups = self.input[self.entry+1].split();
            self.queue = deque(reversed(groups));
            self.next = self.next + 2;
        else: return False;
        return True;
    def read_header(self):
        self.entries = int(self.input[0]);
        self.next = 1;
        self.case = 0;
    def read_file(self):
        f = open('inC');
        self.input = f.readlines();
    def __init__(self):
        self.read_file();
        self.read_header();
        while self.read_entry():
            self.process_entry();


if __name__ == "__main__":
    Problem();

