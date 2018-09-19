#! /usr/bin/python
# Google Code Jam 2012 - Qualification
# Problem A - Speaking in Tongues

mapping = {
    "a" : "y",
    "b" : "h",
    "c" : "e",
    "d" : "s",
    "e" : "o",
    "f" : "c",
    "g" : "v",
    "h" : "x",
    "i" : "d",
    "j" : "u",
    "k" : "i",
    "l" : "g",
    "m" : "l",
    "n" : "b",
    "o" : "k",
    "p" : "r",
    "q" : "z",
    "r" : "t",
    "s" : "n",
    "t" : "w",
    "u" : "j",
    "v" : "p",
    "w" : "f",
    "x" : "m",
    "y" : "a",
    "z" : "q",
    " " : " "
}

convert = lambda x : "".join(map(lambda y : mapping[y], x))

if __name__ == "__main__":
    n = input()
    for x in range(1, n+1):
        print "Case #%d: %s" % (x, convert(raw_input()))



