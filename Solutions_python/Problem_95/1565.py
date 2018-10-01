#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import sys

translation_map = {}
translation_map["a"] = "y"
translation_map["b"] = "h"
translation_map["c"] = "e"
translation_map["d"] = "s"
translation_map["e"] = "o"
translation_map["f"] = "c"
translation_map["g"] = "v"
translation_map["h"] = "x"
translation_map["i"] = "d"
translation_map["j"] = "u"
translation_map["k"] = "i"
translation_map["l"] = "g"
translation_map["m"] = "l"
translation_map["n"] = "b"
translation_map["o"] = "k"
translation_map["p"] = "r"
translation_map["q"] = "z"
translation_map["r"] = "t"
translation_map["s"] = "n"
translation_map["t"] = "w"
translation_map["u"] = "j"
translation_map["v"] = "p"
translation_map["w"] = "f"
translation_map["x"] = "m"
translation_map["y"] = "a"
translation_map["z"] = "q"

translation_map[" "] = " "
translation_map["\n"] = "\n"

def main():
    if len(sys.argv) != 2:
        print "Usage: %s [FILE]\n" % (sys.argv[0])
        exit()

    with open(sys.argv[1]) as input_file:
        t = int(input_file.readline())
        for i, line in zip(xrange(1, t + 1), input_file):
            sys.stdout.write("Case #%d: " % (i))
            for letter in line:
                sys.stdout.write(translation_map[letter])

main()

