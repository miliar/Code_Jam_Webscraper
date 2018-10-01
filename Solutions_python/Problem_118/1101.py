import re
import math

def is_palindrome(number):
    string = str(number)
    for i in range(len(string) / 2):
        if string[i] != string[len(string) - i - 1]:
            #print str(number) + " isn't a palindrome bc %s != %s" % (string[i],string[len(string) - i - 1])
            return False
    return True

def make_palindrome(number):
    string = list(str(number))
    for i in range(len(string) / 2):
        string[len(string) - i - 1] = string[i]
    return int("".join(string))

def inc_palindrome(digit_list,offset=0):   
    length = len(digit_list)
    upper = length / 2 + offset
    lower = length / 2 - offset
    if length % 2 == 0:
        lower -= 1
    if lower < 0:
        new_list = ["0" for i in range(length-1)]
        new_list.insert(0,"1")
        new_list.append("1")
        return int("".join(new_list))
    new_digit = (int(digit_list[upper]) + 1) % 10
    digit_list[upper] = str(new_digit)
    digit_list[lower] = str(new_digit)
    if new_digit == 0:
        return inc_palindrome(digit_list,offset+1)
    return int("".join(digit_list))

def find_next_palindrome(number):
    if not is_palindrome(number):
        return make_palindrome(number)
    return inc_palindrome(list(str(number)))


def count_palindromes(lower,upper):
    count = 0
    cur = find_next_palindrome(lower) if not is_palindrome(lower) else lower
    print "starting at %d" % lower
    while cur <= upper:
        sq = math.sqrt(cur)
        int_sq = int(sq)
        if cur >= lower and is_palindrome(int_sq) and int_sq == sq:
            print "%d is fair and sq" % cur
            count += 1
        else:
            pass
            #print "%d is not because %f isnt" % (cur, sq)
        cur = find_next_palindrome(cur)
        #print "found current %d" % cur
    print "ending at %d" % upper
    return count

def read_game(f):
    bounds = re.split(" ",f.readline())
    return count_palindromes(long(bounds[0]),long(bounds[1]))


def main():
    output = []
    with open("/Users/jyotsnachatradhi/Downloads/C-small-attempt0.in.txt","r") as f:
        trials = f.readline()
        for i in range(int(trials.strip())):
            outline = "Case #%d: %s" % (i+1, read_game(f))
            print outline
            output.append(outline)
    with open("/Users/jyotsnachatradhi/Downloads/fairsquare.txt","w") as f:
        f.write("\n".join(output))


pands = []

def generate_pands():
    cur = 1
    for i in xrange(1000000):
        poss = cur * cur
        if is_palindrome(poss):
            pands.append(poss)
        cur = find_next_palindrome(cur)

def method_2(lower,upper):
    count = 0
    for x in pands:
        if x >= lower and x <= upper:
            count += 1
    return count

if __name__ == "__main__":
    main()