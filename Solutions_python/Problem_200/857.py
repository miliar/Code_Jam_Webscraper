import sys

def first_descend(n):
    if n < 0:
        return False # Not so much defined ...
    s = str(n)
    for i in range(len(s) - 1):
        if int(s[i]) > int(s[i+1]):
            return i
    return -1

def is_tidy(n):
    return first_descend(n) == -1
        

def tatiana(n):
    if is_tidy(n):
        return n
    s = str(n)
    digits = [int(c) for c in str(n)]
    j = first_descend(n)
    i = s.index(s[j])
    digits[i] -= 1 
    for j in range(i+1, len(s)):
        digits[j] = 9
    return digits_to_number(digits)


def digits_to_number(digits):
    return sum([digits[-i-1]*10**i for i in range(len(digits))])


def main(argv):
    T = int(input())
    for i in range(1, T + 1):
        n = int(input())
        print("Case #{}: {}".format(i, tatiana(n)))
        


if __name__ == "__main__":
    main(sys.argv)
