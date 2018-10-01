#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     13/04/2014
# Copyright:   (c) Admin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    f = open(r'C:\Users\Admin\Downloads\A-small-attempt1.in', 'r');
    n=int(f.readline());
    for x in range(0,n):
        line=[];
        line2=[];
        i = int(f.readline());
        for a in range(0,4):
            line1 = f.readline().replace("\n","");
            line.append(line1.split(" "));
        ii = int(f.readline());
        for a in range(0,4):
            line1 = f.readline().replace("\n","");
            line2.append(line1.split(" "));
        good=0;
        for b in range (0,4):
            for c in range(0,4):
                if (line[i-1][b]==line2[ii-1][c]):
                    good=good+1;
                    goodnum=line[i-1][b];
        if (good==0):
            print("Case #"+str(x+1)+": Volunteer Cheated!");
        if (good>1):
            print("Case #"+str(x+1)+": Bad Magician!");
        if (good==1):
            print("Case #"+str(x+1)+": "+str(goodnum));


    pass

if __name__ == '__main__':
    main()
