import operator
from codejam import output

def parse_input(input):
    fin = open(input)
    length, num_words, num_cases = [ int(x) for x in fin.readline().split(" ") ]
    words = [ fin.readline().strip() for x in range(num_words) ]
    
    out = ""
    for i in range(num_cases):
        case  = fin.readline().strip()
        matches = walk(case, words)
        out += "Case #%i: %i\n" % ( i + 1, matches )
    output.to("output-small.txt", out)
    fin.close()

def walk(text, words):
    lst = [ '' ]
    while len(text) != 0:
        if text[0] == '(':
            text = text[1:] # eat parenthesis
            clone = lst[:]
            lst = []
            while text[0] != ')':
                lst.extend(map(lambda x: x + text[0], clone[:]))
                lst = filter(lambda x: x in map(lambda y: y[:len(x)], words), lst)
                text = text[1:]
            text = text[1:] # eat parenthesis
        else:
            next = text.find('(')
            if next == -1: next = len(text)
            lst = map(lambda x: x + text[:next], lst)
            lst = filter(lambda x: x in map(lambda y: y[:len(x)], words), lst)
            text = text[next:]
    return len(lst)

if __name__ == "__main__":
    parse_input("A-small-attempt1.in")