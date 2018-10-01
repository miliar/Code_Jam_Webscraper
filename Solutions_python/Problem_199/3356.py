inputs = []
outputs = []

path = 'A-large.in'
openFile = open(path, 'r')
inputLen = int(openFile.readline())

for _ in range(inputLen):
    line = openFile.readline().split(" ")
    inputs.append([line[0], int(line[1])])
openFile.close()

outputs = inputs
for indO, inp in enumerate(outputs):
    count = 0
    for indI in range(len(inp[0])-inp[1]+1):
        if(inp[0][indI] == '+'):
            pass
        else:
            for pos in range(indI, indI+inp[1]):
                if(outputs[indO][0][pos] == "+"):
                    outputs[indO][0] = outputs[indO][0][:pos] + "-" + outputs[indO][0][pos+1:]
                else:
                    outputs[indO][0] = outputs[indO][0][:pos] + "+" + outputs[indO][0][pos+1:]
            count += 1

    if "-" in outputs[indO][0]:
        outputs[indO].append("IMPOSSIBLE")
    else:
        outputs[indO].append(count)

path = 'output.out'
openFile = open(path, 'w')
for ind, output in enumerate(outputs):
    openFile.write("Case #" + str(ind+1) + ": " + str(output[2]) + "\n")
openFile.close()
