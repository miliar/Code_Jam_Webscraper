import sys;


# reversing a number.
def reverse_int(n):
    return int(str(n)[::-1])


#checking if a particular number is tidy or not.
def checktidy(number):
    l = len(str(number));
    numberlist = [];
    n = reverse_int(number);

    # appending a number to a list
    for i in range(l):
        numberlist.append(int(n)%10)
        n = int(n/10);

    # checking if a list is sorted or not.
    if sorted(numberlist) == numberlist:
        return True;
    else:
        return False;

# method to send eachnumber to check for tidyness.
def tidy(number):
    for x in range(0 , number):
        if(checktidy(number-x)):
            return number-x;
            # break;


# main method
if __name__ == '__main__':

    #reading from a file.
    with open('config.txt') as f:
        n = f.read().splitlines()

    # calling the tidy method on each of the arguments given.
    for i in range(1,int(n[0])+1):
        answer = tidy(int(n[i]));
        print("Case #%d: %d" % (i,answer));
