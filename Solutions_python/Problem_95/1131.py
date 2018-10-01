#! usr/bin/env python

def translate(str):
    translator={' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b','q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p','y': 'a', 'x': 'm', 'z': 'q'}
    s=list(str)
    for i in range(len(s)):
        s[i]=translator[s[i]]
    s="".join(s)
    return s


def main():
    inputfile=open("input.txt",'r+')
    num=int(inputfile.readline())
    x=dict()
    for i in range(1,num+1):
       x[i]=inputfile.readline().strip()

    for i in range(1,num+1):
        print "Case #"+str(i)+": "+str(translate(x[i]))
if __name__=="__main__":
 main()
