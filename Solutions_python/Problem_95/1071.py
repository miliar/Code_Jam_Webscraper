text_file = open("input.txt", "r")
input_text = text_file.readlines()
run_amount = int(input_text[0])
end_result = ""
charmapping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z' : 'q', 'q' : 'z'}
for testcase in range(1,run_amount+1):
    tempstring = ""
    text = list(input_text[testcase])
    for eachletter in text:
        if eachletter in charmapping:
            tempstring = tempstring + charmapping[eachletter]
        else:
            tempstring = tempstring + eachletter
    end_result = end_result + "Case #" + str(testcase) + ": " + tempstring
print end_result
