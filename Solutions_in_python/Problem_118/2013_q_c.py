import os
import sys
import math

class funny_jam:
    IN =sys.stdin;
    case_num =0;
    res_cnt =0;
    
    @classmethod
    def cases(klz):
        return int(klz.IN.readline());

    @classmethod
    def line(klz):
        return klz.IN.readline().strip();
    
    @classmethod
    def out_a_line(klz):
        klz.case_num +=1;
        print "Case #%d: %d" % (klz.case_num, klz.res_cnt);
        klz.res_cnt =0;

    @classmethod
    def is_palindrome(klz, s):
        if len(s) %2:
            center = len(s) /2;
            for ix in xrange(1, center +1):
                if s[center -ix] != s[center +ix]:
                    return False;

            return True;
        else:
            center =len(s) /2;
            shift =1;
            for ix in xrange(center, len(s)):
                if s[ix] != s[ix -shift]:
                    return False;
                shift +=1;
                
            return True;



    @classmethod
    def str_sqrt(klz, n):
        n =math.sqrt(n);
        n=`n`;
        if '.0' ==n[-2:]:
            return n[:-2];
        return n;
        
    @classmethod
    def fair_n_square(klz, n):
        if klz.is_palindrome(`n`):
            if klz.is_palindrome(klz.str_sqrt(n)):
                klz.res_cnt +=1;

    @classmethod
    def solve(klz, l, r):
        for num in xrange(int(l), int(r) +1):
            klz.fair_n_square(num);
        klz.out_a_line();
        
        
def go():
    cases =funny_jam.cases();
    for ct in xrange(cases):
        l, r=funny_jam.line().split();
        funny_jam.solve(l, r);



if __name__ == '__main__':
    stdin =sys.stdin;
    stdout =sys.stdout;
    sys.stdin =open("test.in", "r")
    sys.stdout =open("test.out", "w");
    go();
    sys.stdin.close();
    sys.stdin.close();
    sys.stdin =stdin;
    sys.stdout =stdout;


