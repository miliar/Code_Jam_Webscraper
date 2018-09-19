#!/usr/bin/env python

from __future__ import print_function, division

import math
import os
import os.path
import pprint
import string
import sys


TRANS_PAIRS = (
        ("ejp mysljylc kd kxveddknmc re jsicpdrysi",
         "our language is impossible to understand"),
        ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
         "there are twenty six factorial possibilities"),
        ("de kr kd eoya kw aej tysr re ujdr lkgc jv",
         "so it is okay if you want to just give up"),
        )


def main():
    charMap = {}
    inCharsUnseen = set(string.ascii_lowercase)
    outCharsUnseen = set(string.ascii_lowercase)

    for (inText, outText) in TRANS_PAIRS:
        for (inC, outC) in zip(inText, outText):
            if inC == ' ':
                continue 

            charMap[inC] = outC
            inCharsUnseen.discard(inC)
            outCharsUnseen.discard(outC)

    pprint.pprint(charMap)
    print("unseen in: ", inCharsUnseen)
    print("unseen out: ", outCharsUnseen)


if __name__ == "__main__": main()
