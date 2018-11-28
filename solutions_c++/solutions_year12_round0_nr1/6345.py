#include <iostream>
#include <string>
#include <algorithm>

//#include "trace.h"

/**/void convertChar(char &ch)
    {
    static const char *convertTable="yhesocvxduiglbkrztnwjpfmaq";

    if (ch!=' ') ch=convertTable[ch-'a'];
    }

/**/int main()
    {
    int lineCount;
    std::string line;

    std::cin >> lineCount;
    std::getline(std::cin,line);

    for(int index=0;index<lineCount;++index)
       {
       std::getline(std::cin,line);

       std::for_each(line.begin(),line.end(),convertChar);

       std::cout <<"Case #" <<(index+1) <<": " <<line << std::endl;
       }

    return 0;
    }



/*
our language is impossible to understand
ejp mysljylc kd kxveddknmc re jsicpdrysi

there are twenty six factorial possibilities
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd

so it is okay if you want to just give up
de kr kd eoya kw aej tysr re ujdr lkgc jv


a zoo
y qee

Normal-> Google

a y
b n
c f
d i
e c
f w
g l
h b
i k
j u
k o
l m
m x
n s
o e
p v
q z ..
r p
s d
t r
u j
v g
w t
x h
y a
z q


Normal <- Google

y a
h b
e c
s d
o e
c f
v g
x h
d i
u j
i k
g l
l m
b n
k o
r p
z q
t r
n s
w t
j u
p v
f w
m x
a y
q z
*/

