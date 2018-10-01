
def tidy(input_file, output_file):
    T = int(input_file.readline())

    for case in xrange(1, T + 1):
        N = list(input_file.readline()[0:-1])
        first_flip = len(N)

        for index in range(len(N) - 1, 0, -1):
            if N[index - 1] > N[index]:
                N[index - 1] = str(int(N[index - 1]) - 1)
                first_flip = index

        N[first_flip:len(N)] = ['9'] * (len(N) - first_flip)
        output_file.write("Case #" + str(case) + ": " + str(int(''.join(map(str,N)))) + "\n")

input_file = open("C:\\Users\\doritm\\Desktop\\B-large.in", "r")
output_file = open("C:\\Users\\doritm\\Desktop\\B-large.out", "w")
tidy(input_file, output_file)
input_file.close()
output_file.close()

