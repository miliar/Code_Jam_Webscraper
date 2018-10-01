def update(A,j):
    for i in range(len(A)-1,j-1,-1):
        A[i] = 9;
    A[j-1] = A[j-1] - 1;
    return A;

def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)

input_f = open('B-small-attempt0.in' , 'r');
output_f = open('B_output.txt' , 'w');
T = int(float(input_f.readline()));

for i in range(1,T+1):
    num = int(float(input_f.readline()));
    check = 0;
    A = [int(x) for x in str(num)];
    for j in range(len(A)-1,0,-1):
        if A[j] < A[j-1]:
            A = update(A,j);
            
    tidy = magic(A);
    out = 'Case #' + str(i) + ': ' + str(tidy) + '\n';
    output_f.write(out);
    
            
output_f.close();
input_f.close();
