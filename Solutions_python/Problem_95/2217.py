#!/usr/bin/python
from string import maketrans

infile = open("input.in",'r')
cont = infile.read()
#cont = "3\nejp mysljylc kd kxveddknmc re jsicpdrysi\nrbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\nde kr kd eoya kw aej tysr re ujdr lkgc jv"
data = cont.splitlines()
a = "abcdefghijklmnopqrstuvwxyz"
b = "yhesocvxduiglbkrztnwjpfmaq"
trans = maketrans(a,b)
outfile = open("out.txt",'w')
i=1
while(i<=int(data[0])):
    D = data[i].translate(trans)
    print D;
    i+=1
    outfile.write("Case #"+str(i-1)+": "+str(D)+"\n");
