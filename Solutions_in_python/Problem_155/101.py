#!/usr/bin/python

def readInput(filename):
   content = list();

   with open(filename) as f:
       content = f.readlines()

   count = 0;
   data = list()

   if(len(content) > 0):
       count = content[0];
       for ele in range(1, int(count)+1):
           data.append(content[ele].strip());

   return data;

def printOutput(data):
    index = 1;
    for ele in data:
        print("Case #" + str(index) + ": " + str(ele['count']));
        index = index + 1;


def interpretIo(data):
    count = len(data);
    re = list();
    for ele in data:
        row = dict();
        row['max'] = ele.split(' ')[0];
        row['distribution'] = list(ele.split(' ')[1]);
        row['count'] = 0; #place holder
        re.append(row);
    return re

def getCount(data):
    for row in data:
        sum = 0;
        for i in range(0, int(row['max'])+1):
            sum = sum + int(row['distribution'][i]);
            if(sum<i+1):
                row['count'] = row['count'] + 1;
                sum = sum + 1;

    return data

io = readInput('/home/amit.sharma/code/data/101s');


data = interpretIo(io);

out = getCount(data)
printOutput(out);
