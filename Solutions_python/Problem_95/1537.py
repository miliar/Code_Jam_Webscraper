from sys import stdin


def main():
    n_cases = int(stdin.readline()) 

    for i_case in range(1, n_cases+1):
        line = stdin.readline()

        result = ""

        dict = {
            ' ' : ' ',
            '\n' : '',
            'a' : 'y',
            'b' : 'h',
            'c' : 'e',
            'd' : 's',
            'e' : 'o',
            'f' : 'c',
            'g' : 'v',
            'h' : 'x',
            'i' : 'd',
            'j' : 'u',
            'k' : 'i',
            'l' : 'g',
            'm' : 'l',
            'n' : 'b',
            'o' : 'k',
            'p' : 'r',
            'q' : 'z',
            'r' : 't',
            's' : 'n',
            't' : 'w',
            'u' : 'j',
            'v' : 'p',
            'w' : 'f',
            'x' : 'm',
            'y' : 'a', 
            'z' : 'q'        
        }

        for leter in list(line):
            result += dict[leter]
       

    
        print "Case #" + str(i_case) + ": " + result



if __name__ == '__main__':
    main()
