# -*- coding: utf-8 -*-

"""
A little Python scanner.
Joao Moreno <alph.pt@gmail.com> 2008
"""

from sys import stdin

class Scanner(object):
    from re import compile
    __re_empty = compile(r"\s*$")
    __re_int = compile(r"\s*(\d*)\s?(.*)")
    __re_float = compile(r"\s*((\+|-)?([0-9]+\.?[0-9]*))\s?(.*)")
    __re_word = compile(r"\s*(\S*)\s?(.*)")
    
    def __init__(self, f = stdin):
        super(Scanner, self).__init__()
        self.f = f
        self.line = ""
    
    def __update(self):
        if len(self.line) == 0 or self.__re_empty.match(self.line) is not None:
            self.line = self.f.readline()
    
    def readInt(self):
        return int(self.__read(self.__re_int,1,2))
    
    def readFloat(self):
        return float(self.__read(self.__re_float,1,4))
    
    def readWord(self):
        return self.__read(self.__re_word,1,2)
    
    def __read(self,rexp,content,rest):
        self.__update()
        r = rexp.match(self.line)
        self.line = r.group(rest)
        return r.group(content)
    
    def readChar(self):
        self.__update()
        c = self.line[0]
        self.line = self.line[1:]
        return c
    
    def readLine(self):
        self.__update()
        r = self.line.rstrip()
        self.line = ""
        return r
