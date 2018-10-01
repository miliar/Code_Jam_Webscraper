#!/usr/bin/python3
# Python version >= 3.6


# We go from right to left
def non_decreasing(num_as_string):

    num = [int(x) for x in num_as_string]
    ind = len(num)-1
    while ind > 0:
        if num[ind-1] > num[ind]:
            num[ind:] = [9]*(len(num)-ind)
            num[ind-1] -= 1
        ind -= 1
    if num[0] == 0:
        return "".join(str(x) for x in num[1:])
    else:
        return "".join(str(x) for x in num)


    


if __name__=="__main__":
    T = int(input())

    for case in range(T):
        print(f"Case #{case+1}: ", end="")
        N = input()
        print(f"{non_decreasing(N)}")

        

