#!/usr/bin/python
import sys
from math import *

def findall(L, value):
    result = 0
    i=-1
    try:
        i=L.index( value, i+1 )
        yield i
    except ValueError:
        pass

def f(x):
    return cmp( x[1], x[2] )

def howmanyswitches(num_engines,num_queries,engine_list,query_list):

    num_switches = 0
    #engine list sort by the occurrence in query list
    query_list_len = len( query_list )

    while len(query_list)>0:
        #unique_query_list = [query_list[0]]
        #for i in range(0, len(query_list)):
        #          if cmp( unique_query_list[-1] , query_list[i] ) != 0:
    #                           unique_query_list += query_list[i]
        for engine in engine_list:
              print engine
              print query_list.count(engine)
              if query_list.count(engine) == 0:
                  return num_switches

        query_occurrences = []
        for one_query in set( query_list ):
        #query, frequency, the first index
            query_occurrences += [[ one_query, query_list.count( one_query ), query_list.index( one_query ) ]]
        query_occurrences.sort( lambda x,y: cmp(x[1],y[1]) or cmp(y[2],x[2]) )

        print query_occurrences
        allenginesfound = 0
        if query_occurrences[0][1] != 0:
            num_switches += 1
            search_list = []
            for i in range(0,len(query_list)):
                if not (query_list[i] in search_list):
                    search_list += [query_list[i]]
                if len(search_list) >= len(engine_list):
                    query_list = query_list[i:]
                    break
        #query_list = query_list[ query_occurrences[0][2]+1: ]
        #query_list_len -= query_occurrences[0][2]+1


        print query_list
        print num_switches
    return num_switches
def howmanys(n,A,B,C,D,x0,y0,M):
    output = 0
    X = x0
    Y = y0
    print "(%d,%d)" % (X,Y)
    treelist = [[x0,y0]]
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        print "(%d,%d)" % (X,Y)
        treelist += [[X,Y]]

    #check how many are in a grid point
    combination = []
    length = len(treelist)
    for i in range(0,length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                combination += [[treelist[i],treelist[j],treelist[k]]]

    for i in combination:
        t0,t1,t2 = i
        t0x,t0y=t0
        t1x,t1y=t1
        t2x,t2y=t2
        if (t0x+t0y) == int(t0x+t0y):
            if (t1x+t1y) == int(t1x+t1y):
                if (t2x+t2y) == int(t2x+t2y):
                    print (t0x+t1x+t2x)/3.
                    print (t0y+t1y+t2y)/3.
                    if (t0x+t1x+t2x)/3.== int((t0x+t1x+t2x)/3) and (t0y+t1y+t2y)/3.== int((t0y+t1y+t2y)/3):
                        output += 1
                        #print "(%d,%d) (%d,%d) (%d,%d) (%f,%f)" % (t0x,t0y,t1x,t1y,t2x,t2y,(t0x+t1x+t2x)/3.(t0y+t1y+t2y)/3.)

    return output


def readinputfile( inputfilename, outputfilename ):
    inputread = open( inputfilename , "r" )
    output = open( outputfilename, "w" )

    fileLines = inputread.readlines()
    #print fileLines
    #strip the '\n' character.
    for i in range(0,len( fileLines )):
        fileLines[i] = fileLines[i].strip("\n")

    #print "numCasess=%s" % fileLines[0]

    num_cases = int( fileLines[0] )

    del fileLines[0]

    for i in range(0, num_cases):
        print fileLines[i+0]
        line = fileLines[i].split(" ")
        print line

        n = int(line[0])
        A = int(line[1])
        B = int(line[2])
        C = int(line[3])
        D = int(line[4])
        x0 = int(line[5])
        y0 = int(line[6])
        M = int(line[7])

        print "#=%d A=%d B=%d C=%d D=%d x0=%d y0=%d M=%d\n" %(n,A,B,C,D,x0,y0,M)
        #engine_list = fileLines[1:num_engines+1]num_triangles, A,B,C,D,x0,y0,M= fileLines[i+0][0]

        #del fileLines[:num_engines+1]


        #num_queries = int( fileLines[0] )
        #query_list = fileLines[1:num_queries+1]
        #del fileLines[:num_queries+1]

        #print "Case #%d" % i
        #print engine_list
        #print query_list

        output_value = howmanys(n,A,B,C,D,x0,y0,M)
        output.write( "Case #%d: %d\n" % (i+1,output_value))

def main( inputfilename ):
        outputfilename = inputfilename[0:-3] + ".out"
        #print outputfilename

        readinputfile( inputfilename, outputfilename )

if __name__ == '__main__':
        if len(sys.argv) == 2:
                main( sys.argv[1] ) #input filename
