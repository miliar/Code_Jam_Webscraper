#f = open('B-small-attempt0.in')
f = open('B-large.in')
#f = open('test.in')
count = int(f.readline())
output = ''

def check():
    global matrix,rowCount,columnCount
    currentRow = 0
    currentMin = 100
    for i in range(0,rowCount):
        tempMin = min(matrix[i])
        if tempMin < currentMin:
            currentMin = tempMin
            currentRow = i
    minIndex = matrix[currentRow].index(currentMin)
    if matrix[currentRow].count(currentMin) == len(matrix[currentRow]):
        del matrix[currentRow]
        rowCount -= 1
        if rowCount == 0:
            return True
        return check()
    else:
        for j in range(0,rowCount):
            if matrix[j][minIndex] != currentMin:
                return False
            del matrix[j][minIndex]
        columnCount -= 1
        if columnCount == 0:
            return True
        return check()

for i in range(0,count):
    rowAndColumn = f.readline().split()
    rowCount = int(rowAndColumn[0])
    columnCount = int(rowAndColumn[1])
    matrix = [[]] * rowCount
    for j in range(0,rowCount):
        matrix[j] = f.readline().split()
        for k in range(0,len(matrix[j])):
            matrix[j][k] = int(matrix[j][k])
    if check():
        output += 'Case #' + str(i+1) + ': YES\n'
    else:
        output += 'Case #' + str(i+1) + ': NO\n'


print(output)
newf = open('output.txt','w')
newf.write(output)
#Case #1: YES
#Case #2: NO
#Case #3: YES
