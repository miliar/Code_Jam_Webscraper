import io
#from itertools import chain

input_stream = io.StringIO('''3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1''')

def read_lawn(f):
    lawn = []
    N, M = [int(v) for v in f.readline().split()]
    for n in range(N):
        line = f.readline()
        lawn.append([int(v) for v in line.split()])
    return lawn

def process_lawn(lawn):
    for i, row in enumerate(lawn):
        for j, element in enumerate(lawn[i]):
            if any(v > element for v in row) and any(v > element for v in get_column_elements(lawn, j)):
                return False
    return True

def get_column_elements(matrix, j):
    for row in matrix:
        yield row[j]

def main(input_stream):
    for i in range(int(input_stream.readline())):
        lawn = read_lawn(input_stream)
        result = process_lawn(lawn)
        message = {
            True: 'YES',
            False: 'NO',
        }[result]
        print('Case #%d: %s' %(i+1, message))
    
    

if __name__ == '__main__':
    #main(input_stream)
    import sys
    main(open(sys.argv[1]))