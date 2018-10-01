#!/usr/bin/env python
#
# Copyright (c) 2013 NetApp, Inc.
# All rights reserved.
#
"""
"""

from __future__ import print_function
import argparse
import getpass
import glob
import imp
import itertools
import logging
import pkg_resources
import pkgutil
import sys
import re
import ystockquote
import requests
import threading
from multiprocessing import Process
import time

logger = logging.getLogger(__name__)

def main():
    streamformat = "%(message)s"
    logging.basicConfig(level=logging.INFO,
                        format=streamformat)

    data = sys.stdin.readlines()
    i = 0
    nums = [int(n) for n in data[i].split()]
    num_test_cases = nums[0]
    for j in range(num_test_cases):
        nums_1 = []
        nums_2 = []
        i = i + 1
        nums = [int(n) for n in data[i].split()]
        first_choice = nums[0]
        i = i + 1
        nums_1.append([int(n) for n in data[i].split()])
        i = i + 1
        nums_1.append([int(n) for n in data[i].split()])
        i = i + 1
        nums_1.append([int(n) for n in data[i].split()])
        i = i + 1
        nums_1.append([int(n) for n in data[i].split()])
        i = i + 1
        nums = [int(n) for n in data[i].split()]
        second_choice = nums[0]
        i = i + 1
        nums_2.append([int(n) for n in data[i].split()])
        i = i + 1
        nums_2.append([int(n) for n in data[i].split()])
        i = i + 1
        nums_2.append([int(n) for n in data[i].split()])
        i = i + 1
        nums_2.append([int(n) for n in data[i].split()])
        intersection = set(nums_1[first_choice-1]).intersection( set(nums_2[second_choice-1]) )
        if len(intersection) == 1:
            logger.info("Case #{0}: {1}".format(j+1, intersection.pop()))
        elif len(intersection) > 1:
            logger.info("Case #{0}: Bad magician!".format(j+1))
        else:
            logger.info("Case #{0}: Volunteer cheated!".format(j+1))
        

if __name__ == "__main__":
    main()
