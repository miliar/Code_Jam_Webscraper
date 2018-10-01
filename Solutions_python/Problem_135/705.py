#!/usr/bin/python
#! - * - coding: utf-8 - * -

class Magic(object):
    def __init__(self):
        self.f, self.frows = self.get_input()
        self.s, self.srows = self.get_input()
    def get_input(self):
        num = self.get_int() -1
        row = []
        for i in range(4):
            row.append(raw_input().split())
        return num, row[num]
    def get_int(self):
        data = int(raw_input())
        return data
    def start(self):
        count = 0
        for data in self.frows:
            if data in self.srows:
                count += 1
                answer = data
        if count == 0:
            return "Volunteer cheated!"
        elif count == 1:
            return answer
        else: 
            return "Bad magician!"


if __name__ == "__main__":  
    tc = int(raw_input())
    for i in range(tc):
        obj = Magic()
        print "Case #%d: %s" % (i+1, obj.start())
  
