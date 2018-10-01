def forward(N_list):
    for i in range(len(N_list)):
        if i + 1 < len(N_list) and N_list[i] > N_list[i+1]:
            N_list[i] -= 1
            for j in range(i+1,len(N_list)):
                N_list[j] = 9
            return forward(N_list)
    return N_list


with open("input.txt","r") as reader, open("output.txt","w") as writer:
    cases = int(reader.readline())
    for cs in range(1,cases+1):
        N_list = list(reader.readline().strip())
        N_list = map(int,N_list)
        N_forward = forward(N_list)
        answer = int("".join(map(str,N_forward)))
        writer.write("Case #"+str(cs)+": "+str(answer)+"\n")


