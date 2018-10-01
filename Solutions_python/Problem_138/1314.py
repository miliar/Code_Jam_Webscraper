from common import parse_input, log_output

@parse_input(file_name='D-large.in')
@log_output(file_name='D-large.out')
def main(f=None, t=None):
    for tc in range(t):
        f.readline()
        naomi = sorted(map(lambda ip: float(ip), f.readline().rstrip().split(' ')))
        ken = sorted(map(lambda ip: float(ip), f.readline().rstrip().split(' ')))

        index_naomi = 0
        wins_deceitful = 0
        for val in ken:
            while index_naomi != len(naomi):
                if naomi[index_naomi] > val:
                    wins_deceitful += 1
                    index_naomi += 1
                    break
                else:
                    index_naomi += 1
            if index_naomi == len(naomi):
                break

        wins_fair = 0
        new_ken = ken
        for val in reversed(naomi):
            val_ken = next((i for i, v in enumerate(new_ken) if v > val), None)
            if val_ken is not None:
                del new_ken[val_ken]
            else:
                wins_fair += 1

        print 'Case #%d: %d %d' % (tc + 1, wins_deceitful, wins_fair)

if __name__ == '__main__':
    main()

