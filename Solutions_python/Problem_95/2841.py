#Author: Parker Olson
#Date: 4/13/2012

def main():
    number = int(input())
    string = input();
    trans = translate(string, number);
    print(trans);


def translate(s, n):
    trans = ""
    i = 0
    count = 1;
    transStr = []
    while i < len(s):
        u = 0
        char = s[i]
        if char == 'a':
            transStr.append('y')
        elif char == 'b':
            transStr.append('h')
        elif char == 'c':
            transStr.append('e')
        elif char == 'd':
            transStr.append('s')
        elif char == 'e':
            transStr.append('o')
        elif char == 'f':
            transStr.append('c')
        elif char == 'g':
            transStr.append('v') 
        elif char == 'h':
            transStr.append('x')
        elif char == 'i':
            transStr.append('d')
        elif char == 'j':
            transStr.append('u')
        elif char == 'k':
            transStr.append('i')
        elif char == 'l':
            transStr.append('g')
        elif char == 'm':
            transStr.append('l')
        elif char == 'n':
            transStr.append('b')
        elif char == 'o':
            transStr.append('k')
        elif char == 'p':
            transStr.append('r')
        elif char == 'q':
            transStr.append('z')
        elif char == 'r':
            transStr.append('t')
        elif char == 's':
            transStr.append('n')
        elif char == 't':
            transStr.append('w')
        elif char == 'u':
            transStr.append('j')
        elif char == 'v':
            transStr.append('p')
        elif char == 'w':
            transStr.append('f')
        elif char == 'x':
            transStr.append('m')
        elif char == 'y':
            transStr.append('a')
        elif char == 'z':
            transStr.append('q')
        elif char == 'A':
            transStr.append('Y')
        elif char == 'B':
            transStr.append('H')
        elif char == 'C':
            transStr.append('E')
        elif char == 'D':
            transStr.append('S')
        elif char == 'E':
            transStr.append('O')
        elif char == 'F':
            transStr.append('C')
        elif char == 'G':
            transStr.append('V')
        elif char == 'H':
            transStr.append('X')
        elif char == 'I':
            transStr.append('D')
        elif char == 'J':
            transStr.append('U')
        elif char == 'K':
            transStr.append('I')
        elif char == 'L':
            transStr.append('G')
        elif char == 'M':
            transStr.append('L')
        elif char == 'N':
            transStr.append('B')
        elif char == 'O':
            transStr.append('K')
        elif char == 'P':
            transStr.append('R')
        elif char == 'Q':
            transStr.append('Z')
        elif char == 'R':
            transStr.append('T')
        elif char == 'S':
            transStr.append('N')
        elif char == 'T':
            transStr.append('W')
        elif char == 'U':
            transStr.append('J')
        elif char == 'V':
            transStr.append('P')
        elif char == 'W':
            transStr.append('F')
        elif char == 'X':
           transStr.append('M' )
        elif char == 'Y':
            transStr.append('A')
        elif char == 'Z':
            transStr.append('Q')
        elif char == '\n':
            if count <= n:
                transStr.append('\nCase #' + str(count) + ": ")
                count += 1
        else:
            transStr.append(char)
        i += 1
    return "".join(transStr);

main()
