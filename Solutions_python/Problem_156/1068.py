#!/usr/bin/python
# coding: utf-8

import sys
import os
import re
import datetime
import math
import argparse


class Exo2Plate(object):

    Tcase = 0
    filename = "B-small-attempt4.in"
    #filename = "test1.txt"
    filenameout = "output2.txt"

    maxpancakeinplate = 0
    maxpancakeinplateindex = 0
    secondmaxpancake = 0
    secondmaxpancakeindex = 0
    minpancakeinplate = 1000
    minpancakeinplateindex = 0
    table = []
    
    def __init__(self):
        self.exosolution2()


    def exosolution2(self):
        with open(self.filename, 'r') as f:
             read_data = f.readlines()
        f.closed

        with open(self.filenameout, 'w') as fileout:
            for index,row in enumerate(read_data):
                if index == 0 :
                    self.Tcase = row
                    print "Tcase:" + self.Tcase
                else:
                    if index > self.Tcase:
                        print "Erreur too big"
                    else:
                        self.parse_data(row, index, fileout)

            
    def should_divided(self):
        print self.table
        if self.maxpancakeinplate < 4:
            return False
        savedtime = 0
        
        if (len(self.table) > 1) and (self.maxpancakeinplate - 1 >= self.table[len(self.table) - 2]) and self.maxpancakeinplate != 9:
            return True
        if (self.maxpancakeinplate % 3 == 0 and (self.maxpancakeinplate - 2 >= self.table[len(self.table) - 2]) and self.maxpancakeinplate != 6):
            savedtime = int((self.maxpancakeinplate-2) - math.ceil((self.maxpancakeinplate/3.0)))
        else :
            savedtime = int((self.maxpancakeinplate-1) - math.ceil((self.maxpancakeinplate/2.0)))

        if savedtime > len(self.table)-1:
            return True
        if (self.maxpancakeinplate % 3 == 0 and self.maxpancakeinplate != 6 and self.maxpancakeinplate - 2 >= self.table[len(self.table) - 2]):
            return True

        print self.table[len(self.table)-(savedtime)]
        print int(math.ceil((self.maxpancakeinplate/2.0)))

        if self.maxpancakeinplate % 3 == 0 and self.maxpancakeinplate != 6:
            if self.table[len(self.table)- 2] == 9 and self.table[len(self.table)- 3] == 6:
                return True
            if self.table[len(self.table)-(savedtime+1)] > int(math.ceil((self.maxpancakeinplate/2.0))):
                return False
            else:
                return True

        print self.table[len(self.table)-(savedtime)]
        print int(math.ceil((self.maxpancakeinplate/2.0)))   
            
        if self.table[len(self.table)-(savedtime+1)] > int(math.ceil((self.maxpancakeinplate/2.0))):
            return False
        else:
            return True

            

    def parse_data(self, linetoparse, testcaseid, fileout):
        #print linetoparse
        if ((testcaseid - 1) % 2 == 0):
            self.numberofplatesnonempty = linetoparse
        else:
            index = 0
            self.table = []
            for fullplates in xrange(int(self.numberofplatesnonempty)):
                plate = int((linetoparse.split(' ')[fullplates]).strip())   
                self.table.append(plate)
                

            self.get_information()
            
            numberofminutes = 1
            ongoing = False
            print str(testcaseid/2)
            while(1):
                platesnotempty = False
 
                if((not ongoing) and self.should_divided()):
                    print "I divide"

                    if (len(self.table) == 1 and self.maxpancakeinplate % 3 == 0):
                        self.table[len(self.table)-1] = self.maxpancakeinplate/3
                        self.table.append(self.maxpancakeinplate/3)
                        self.table.append(self.maxpancakeinplate/3)
                        numberofminutes = numberofminutes + 1
                    elif (self.maxpancakeinplate % 3 == 0):
                        if (self.maxpancakeinplate == 6):
                            self.table[len(self.table)-1] = int(math.ceil((self.maxpancakeinplate/2.0)))
                            self.table.append(int(math.floor((self.maxpancakeinplate/2.0))))
                        elif self.maxpancakeinplate == 9 and self.table[len(self.table)-2] == 6 and (len(self.table) < 3 or self.table[len(self.table)-3] < 5):
                            self.table[len(self.table)-1] = self.maxpancakeinplate/3
                            self.table.append(self.maxpancakeinplate/3)
                            self.table.append(self.maxpancakeinplate/3)
                            numberofminutes = numberofminutes + 1
                        elif(int(math.ceil((self.maxpancakeinplate/2.0)))-1 > self.table[len(self.table)-2]):                         
                            self.table[len(self.table)-1] = self.maxpancakeinplate/3
                            self.table.append(self.maxpancakeinplate/3)
                            self.table.append(self.maxpancakeinplate/3)
                            numberofminutes = numberofminutes + 1
                        elif ((self.maxpancakeinplate * 2.0 / 3.0) == self.table[len(self.table)-2]) and self.table[len(self.table)-3] < 5:
                            self.table[len(self.table)-1] = self.maxpancakeinplate/3
                            self.table.append(self.maxpancakeinplate/3)
                            self.table.append(self.maxpancakeinplate/3)
                            numberofminutes = numberofminutes + 1
                        else:
                            self.table[len(self.table)-1] = int(math.ceil((self.maxpancakeinplate/2.0)))
                            self.table.append(int(math.floor((self.maxpancakeinplate/2.0))))   
                    else:
                        self.table[len(self.table)-1] = int(math.ceil((self.maxpancakeinplate/2.0)))
                        self.table.append(int(math.floor((self.maxpancakeinplate/2.0))))                  
                else:
                    ongoing = True

                    for index, data in enumerate(self.table):
                        if(data > 0):
                            self.table[index] = data - 1

                if max(self.table) == 0:
                    stringtowrite = "Case #" + str(testcaseid/2) + ": " + str(numberofminutes) + "\n"
                    fileout.write(stringtowrite)
                    break
                numberofminutes = numberofminutes + 1
                
                self.get_information()

    def get_information(self):
        self.table.sort()
        print self.table
        self.maxpancakeinplate = self.table[len(self.table)-1]





            

### MAIN ###
if __name__ == "__main__":
	foo = Exo2Plate()
