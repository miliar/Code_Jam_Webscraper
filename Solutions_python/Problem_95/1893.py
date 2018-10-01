#!/usr/bin/env python



###############################################################################
##  *****     *****    Initial constants    *****     *****
###############################################################################
globals()["PROP_CONFIG_FILENAME"] = "propertyConfigFile"
globals()["PACKAGE_NAME"] = 'image_adaptor'



###############################################################################
##  *****     *****    External modules to import    *****     *****
###############################################################################
# ****   Standard Python Utility Modules
#==============================================================================
import os
import sys

import string



###############################################################################
##  *****     *****    PROCESSING FUNCTIONS     *****     *****
###############################################################################

def loadTests(file_name):
    f = open(file_name, 'r')
    f.readline()

    tests = f.readlines()

    f.close()

    return tests

def saveRes(file_name, results):

    f = open(file_name, 'w')

    for i in range(1, len(results)+1):
        f.write("Case #" + str(i) + ": " + str(results[i-1]) + "\r\n")

    f.close()

    return True




###############################################################################
##  *****     *****    MAIN FUNCTION OF THE CODE     *****     *****
###############################################################################


def mainFunction(inputFile):
    tests = loadTests(inputFile)

    translation = {' ':' '}

    print "Inserting some example lines to learn:"

    exampleLines = ["z", "y qee", "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
    exampleResult = ["q", "a zoo", "our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]

    for ex in range (0, len(exampleLines)):
        longitud = len(exampleLines[ex])
        for index in range(0, longitud):
            translation[exampleLines[ex][index]] = exampleResult[ex][index]
    results = []
    for line in tests:
        newLine = ""
        for letter in line[:-1]:
            if letter in translation:
                newLine = newLine + translation[letter]
            else:
                newLine = newLine + '?'
        results.append(newLine)

    print "Before:"
    for resLine in tests:
        print resLine
    print "***********************AFTER****************"
    for resLine in results:
        print resLine

    saveRes(inputFile + ".out", results)
    return 0





###############################################################################
##  *****    *****    ENTRY POINT FOR STARTING THE CODE    *****    *****
###############################################################################

if __name__ == '__main__':
    try:
        inFile = "PrATest.in"
        if len(sys.argv) > 1:
            inFile = sys.argv[1]
#        else:
#            print "At least the filename is needed!"
        endValue = mainFunction(inFile)
    except Exception as e:
        print "WHOLE-SCOPE EXCEPTION - NODE SHUTTING DOWN"
        print ("Error: %s."%e).center(80, '*')
