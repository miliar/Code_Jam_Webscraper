#!/usr/bin/python
# Filename: myFileIO.py

'''
Created on May 8, 2010

This module provides utility functions to read data from file;
and to write data to file

@author: zeest
'''

# globals
SPACE = ' '
CR = '\r'
LF = '\n'
DLMTR = LF
SEP = SPACE

PREFIX = "Case #"
SUFFIX = ":"

DEBUG = False

def readFromFile (filepath, sep = SEP, dlmtr = DLMTR):
    ''' Loads data from file.
    
    Gets a file path and returns 2-dimensional list. '''

    fOK = True # flag to say everything all right
    rows = [] # list to contain file rows
    data = [] #list to contain tokenzied values
    tokens = [] # values in a row
    
    global DEBUG
    
    if filepath == '':
        fOK = False

    if fOK:
        try: # Read file >>>
            pFile = open(filepath, 'r')
       
            try:# Read from File into List
                while True: 
                    row = pFile.readline() 
                    if len(row) == 0: # Zero length indicates EOF 
                        break 
                    row = row.strip() # remove all whitespace
                    rows.append(row) 
            finally:    
                # Close file ref
                pFile.close()
        except IOError:
            fOK = False # some error occurred
        
    if fOK:    
        # Tokenize data from file >>>
        total = len(rows)
        
        for i in range(0, total):   #for line in allrows:
            row = rows[i]
            if DEBUG:
                print row
            tokens = row.split(sep)
            data.append(tokens)
    
    # clear unused lists
    tokens = []
    rows = [] 
    
    return data;
    #end of function readFromFile
     
def writeToFile (filepath, data, includeSerial = True, prefix = PREFIX, suffix = SUFFIX, sep = SEP, dlmtr = DLMTR ):  
    ''' Writes data to a file in required output format.
    
    Gets a file path and a 1-dimensional list. '''

    fOK = True # flag to say everything all right
    
    if filepath == '':
        fOK = False    
     
    if fOK:
        try: # Open file >>>
            pFile = open(filepath, 'w')
            
            try:
                total = len(data) # number of rows
        
                for i in range(0, total):
                    row = ''
                    if includeSerial:
                        row = PREFIX + str(i+1) + SUFFIX + sep
                        
                    row = row + str(data[i])
                    pFile.write(row + dlmtr)
              
            finally:         
                    # Close file ref
                    pFile.close()
        except:
            fOK = False
   
    return fOK;
    #end of function writeToFile
       
# End of myFileIO.py