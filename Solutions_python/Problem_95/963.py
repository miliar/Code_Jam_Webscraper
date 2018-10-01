googlerese_to_english = {'y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z',' ':' ','\n':'\n'}

def parse_file():
    input_file = open("A-small-attempt0.in", "r")
    input_string = []
    input_string.append(input_file.readline())
    numTestCases = int(input_string[0])
    for x in range(0,numTestCases):
        input_string.append(input_file.readline())
    input_file.close()
    return input_string

def print_input_string(input_array):
    for x in range(0,len(input_array)):
        print input_array[x],

def translate_line(x):
    y = ''
    i = 0
    while (x[i:i+1]!=''):
        y += googlerese_to_english[x[i:i+1]]
        i += 1
    print y,
    return y

def output_to_file(input_array):
    f = open("./output.txt", "w")
    stuff = ''
    for x in range(1, len(input_array)):
        stuff = translate_line(input_array[x])
        stuff = "Case #" + str(x) + ": " + stuff
        f.write(stuff)

inputstring = parse_file()
output_to_file(inputstring)
#print_input_string(inputstring)
#for x in range(1, len(inputstring)):
#    translate_line(inputstring[x])

