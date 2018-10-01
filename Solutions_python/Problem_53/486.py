def period(N):
    return 2**N;

def res(N, K):
    p = period(N);
    return K % p == p - 1;


fin = open("A-large.in", "r");
fout = open("A-large.out", "w");

T = int(fin.readline());

for t in range(T):
    (N, K) = eval("(" + fin.readline().replace(" ", ",") + ")");

    answer = "OFF";
    if (res(N, K)):
        answer = "ON";
    fout.write("Case #" + str(t+1) + ": " + answer + "\n")

fout.close();
