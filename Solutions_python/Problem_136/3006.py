#!/usr/bin/python

import re
import sys
import argparse
import csv
import urllib2
from decimal import *
import math

def readArgs():
  getOpt = argparse.ArgumentParser()
  
  getOpt.add_argument('-i', '--inFile',
      help='Read from file specified',
      action="store", nargs=1, required=True )

#  group = getOpt.add_mutually_exclusive_group()
#  group.add_argument('-m', '--male',
#      help='Write output to file: [inputfile].summary w/ male names',
#      action="store_true")
#  group.add_argument('-f', '--female',
#      help='Write output to file: [inputfile].summary w/ female names',
#      action="store_true")

  getOpt.add_argument('-o', '--outFile',
      help='File where you want to output the results',
      action="store", nargs=1, required=True )

  return getOpt.parse_args()


def getCallNum(bibnum, pattern):
 
  url="http://www.aadl.org/catalog/record/{bib}".format(bib=bibnum)
  response = urllib2.urlopen(url)
  the_page = response.read()
  
  match = pattern.findall(the_page) 

  if(not match):
    return ''
  else:
   
    if(len(match) > 1):
      print 'More than 1 match found!!'
  
    return match[0]
      

def main():

  args = readArgs()
  
  count = 0
  
  pattern = re.compile('Call number:\s*<strong>\s*<a.*>\s*(.*)</a>')
  
  with open(args.inFile[0], 'rb') as f_in, open(args.outFile[0], 'wb') as f_out:
    getcontext().prec = 10 
    
    numTests = int( f_in.readline().strip('\n') )

    for idx in xrange(numTests):
      
      test_raw = f_in.readline().strip('\n').split()
      
      test = [ Decimal(val) for val in test_raw ]
      
      C = Decimal( test[0] )
      F = Decimal( test[1] )
      X = Decimal( test[2] )
      
      #print C, F, X
      
      minFact = math.ceil( (F*X - 2*C - C*F) / (C*F) )
  

      minFact = Decimal(max(0, minFact))

      #print 'Min Factories:', minFact
      
      count = 0
      frac = Decimal(0.0)
      
      while True:
        
        if(count < minFact):
          
          frac = frac + ( Decimal(1) / Decimal(2 + F  * count) )

        else:
          break
        
        count = count + 1
      
      final = Decimal(C * frac) + ( Decimal(X) / Decimal(2 + (F * minFact)) )

      #print final

      f_out.write('Case #' + str(idx+1) + ': ' + str(final) + '\n')
      


        










if __name__ == '__main__':
  main()
