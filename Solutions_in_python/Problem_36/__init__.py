from codejam import output

def parse_input(input):
    fin = open(input)
    cases = int(fin.readline())
    out = ""
    for i in range(cases):
        line  = fin.readline()
        times = search_str("welcome to code jam", line)
        out += "Case #%i: %04i\n" % ( i + 1, times )
    output.output_to("output-small.txt", out)
    fin.close()

def search_str(target, line, found=0):
    if len(target) == 0:
        return found + 1
    char = target[0]
    partial = ""
    for index, char in enumerate(line):
        if char == target[0]:
            found = search_str(target[1:], line[index:], found)
    return found

if __name__ == "__main__":
    parse_input("C-small-attempt2.in")