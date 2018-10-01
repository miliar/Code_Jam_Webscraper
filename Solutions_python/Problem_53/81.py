def is_on(N, K):
    return K % (2**N) == 2**N - 1

def main():
    n = int(raw_input())
    for i in range(1, n+1):
        N,K = map(int, raw_input().split())
        out = "OFF"
        if is_on(N, K):
            out = "ON"
        print "Case #%d: %s" % (i, out)

if __name__ == "__main__":
    main()
