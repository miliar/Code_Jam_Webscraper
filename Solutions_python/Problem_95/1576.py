GoogToEng = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

numTests = input('')

response = []

for i in range(0,numTests):
    line = str(raw_input(''))

    output = ""

    for j in line:
        output = output + GoogToEng[j]

    response.append(output)

c = 0
for i in response:
    print "Case #" + str(c) + ": " + i
    c = c + 1
