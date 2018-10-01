import sys

def solve(N):

    list_of_ints = [int(i) for i in str(N)]

    i=0
    while i < len(list_of_ints)-1:
        if list_of_ints[i]>list_of_ints[i+1]:
            list_of_ints[i]-=1
            for j in range(i+1,len(list_of_ints)):
                list_of_ints[j]=9
            i=-1
        i+=1

    tidy_n = int(''.join([str(p) for p in list_of_ints]))

    return tidy_n

if __name__ == '__main__':
     in_path = sys.argv[1]
     out_path = sys.argv[2]

     with open(in_path, "r") as f:
          N = int(f.readline())

          out = open(out_path, 'w')

          for i in range(N):
               out.write('Case #'+(str(i+1))+": ")
               new = f.readline().split(" ")

               N = int(new[0])

               out.write(str(solve(N)))
               out.write('\n')

          out.close()