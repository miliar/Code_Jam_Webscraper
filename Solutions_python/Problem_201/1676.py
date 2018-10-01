from heapq import heappush as push, heappop as pop

def main():
    T = int(input())
    for case in range(1, T+1):
        N, K = [int(i) for i in input().split()]
        heap = []
        push(heap, -N)
        while(K > 1):
            K -= 1
            gap = -1*pop(heap)  # heap has flipped signs
            gap -= 1 
            min_half = gap//2
            max_half = min_half + (gap % 2)
            push(heap, -1*min_half)
            push(heap, -1*max_half)

        gap = -1*pop(heap)
        gap -= 1
        min_half = gap//2 
        max_half = min_half + (gap % 2)
        print('Case #{}: {} {}'. format(case, max_half, min_half))
        
if __name__ == '__main__':
    main()
