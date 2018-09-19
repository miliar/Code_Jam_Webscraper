decode = {
    "y":"a",
    "n":"b",
    "f":"c",
    "i":"d",
    "c":"e",
    "w":"f",
    "l":"g",
    "b":"h",
    "k":"i",
    "u":"j",
    "o":"k",
    "m":"l",
    "x":"m",
    "s":"n",
    "e":"o",
    "v":"p",
    "z":"q",
    "p":"r",
    "d":"s",
    "r":"t",
    "j":"u",
    "g":"v",
    "t":"w",
    "h":"x",
    "a":"y",
    "q":"z",
    " ":" "
}

input = open("input.txt", "r")
output = open("output1.txt","w")
testcases = int(input.readline())
count = 1
while count <= testcases:
	out_line = "Case #"+repr(count)+": "
	in_line = input.readline()
	for i in range(len(in_line)):
		out_line = out_line + decode.get(in_line[i],"")
	output.write(out_line+"\n")
	count = count+1
