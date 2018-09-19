def readFile(filename=None):
    if (filename == None):
        return None
    f = open(filename)
    content = f.readlines()
    f.close()
    return content


def storeLines(lines, filename=None):
    if (filename == None):
        return None
    f = open(filename, 'w')
    for line in lines:
        f.write(line + '\n')
    f.close()
    print 'Data successfully stored in ' + filename + '!'


def splitString(string, separator=' '):
    return str.split(string, separator)


def parseMatrix(lines, startIndex, rowsSize, separator=' ', forceInteger=False):
    xSize = len(splitString(lines[startIndex], separator))
    ySize = int(rowsSize)
    matrix = [[0 for i in range(xSize)] for j in range(ySize)]
    for i in range(xSize):
        lineEntry = splitString(lines[i + startIndex], separator)
        for j in range(ySize):
            matrix[i][j] = (lineEntry[j], int(lineEntry[j]))[forceInteger]

    return matrix


def appendResult(entry, result=[], prefix='Case #', firstIndex=1):
    content = prefix + str(firstIndex + len(result)) + ': ' + entry
    result.append(content)
    return result


def getColumn(matrix, index):
    return [row[index] for row in matrix]


def getRow(matrix, index):
    return matrix[index]