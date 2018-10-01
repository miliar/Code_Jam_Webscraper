

class OversizedPancakeFlipper:
    @staticmethod
    def solve(pancakes, k):
        pancakes = list(pancakes)

        def flip(x):
            return '+' if x == '-' else '-'

        flip_count = 0
        size = len(pancakes)
        for i in range(0, size):
            if pancakes[i] == '-':
                if i+k-1 >= size:
                    return 'IMPOSSIBLE'
                for j in range(0, k):
                    pancakes[i+j] = flip(pancakes[i+j])

                flip_count += 1

        return flip_count

    @staticmethod
    def main():
        t = int(input())
        for i in range(0, t):
            s = input()
            pancakes, k = s.split(' ')
            print('Case #%s: %s' % (i+1, OversizedPancakeFlipper.solve(pancakes, int(k))))

if __name__ == "__main__":
    OversizedPancakeFlipper.main()
