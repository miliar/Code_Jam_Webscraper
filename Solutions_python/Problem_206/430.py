#!/usr/bin/python
# coding: utf-8

import sys
import os
import re
import datetime
import argparse


class Exo1(object):

    listcase = []
    Tcase = 0
    filename = "A-large.in"
    filenameout = "outputbig.txt"
    def __init__(self,args):
        self.filename = args['inputfilename']
        self.filenameout = args['outputfilename']
        self.exosolution1()


    def exosolution1(self):
        with open(self.filename, 'r') as f:
            #f.readlines()
            index = 0
            with open(self.filenameout, 'w') as fileout:
                data = f.readline()
                    
                while data:
                    #print data
                    if index == 0 :
                        self.Tcase = data
                    else:
                        case = data.split()
                        totalhorse = int(case[1])
                        totalroad = int(case[0])
                        table = []
                        previous = 0
                        for i in range(totalhorse):
                            horse = f.readline().split()
                            hour = float(totalroad-int(horse[0]))/float(int(horse[1]))
                            previous = max(previous, hour)
                        #self.parse_data(row, index, fileout)
                        minspeed = totalroad/previous
                        stringtowrite = "Case #" + str(index) + ": " + str(minspeed) + "\n"
                        fileout.write(stringtowrite)
                    index = index + 1
                    data = f.readline()


def initialize_args():
    parser = argparse.ArgumentParser(description='Nagios Sensor Status')
    parser.add_argument('-i', dest='inputfilename', help='Input Filename', required=True)
    parser.add_argument('-o', dest='outputfilename', help='Output Filename', required=True)
    parser.set_defaults(feature=False)
    args = vars(parser.parse_args())
    return args


### MAIN ###
if __name__ == "__main__":
    args = initialize_args()
    foo = Exo1(args)
