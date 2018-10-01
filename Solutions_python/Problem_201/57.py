from collections import defaultdict
import sys

def find_last_sequence(N, K):
    sequences = defaultdict(int)
    sequences[N] = 1
    waiting_poeple = K
    while True:
        seq, count = max(sequences.items())
        if count >= waiting_poeple:
            return seq
        waiting_poeple -= count
        del sequences[seq]
        sequences[seq/2] += count
        sequences[(seq-1)/2] += count

if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        N, K = [int(part) for part in sys.stdin.readline().split()]
        assert 1 <= K <= N
        seq = find_last_sequence(N, K)
        print "Case #%d: %d %d" % (i+1, seq/2, (seq-1)/2)
