from math import *
def probB():
    f=open('input.txt','r')
    new=open('answer.txt','w')
    for tc in xrange(1, int(f.readline())+1):
        # Get input
        line=f.readline()
        array=line.split(" ")
        rows=int(array[0])
        columns=int(array[1])
        field=[]
        for i in xrange(0,rows):
            field.append([int(x) for x in f.readline().split(' ')])

        # Check the 1's
        answer=checkField(field, rows, columns)
        if answer:
            new.write('Case #%d: %s' % (tc,'YES')+"\n")
        else:
            new.write('Case #%d: %s' % (tc,'NO')+"\n")

def checkField(field, rows, columns):
    for row in xrange(0,rows):
        for column in xrange(0,columns):
            if tooHighColumn(field, column, field[row][column]) and tooHighRow(field, row, field[row][column]):
                return False
    return True

def tooHighColumn(field, column, value):
    for row in xrange(0, len(field)):
        if field[row][column]>value:
            return True
    return False


def tooHighRow(field, row, value):
    for column in field[row]:
        if column>value:
            return True
    return False         
