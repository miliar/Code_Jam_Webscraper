import sys

def naomi_war_game_score(naomi_blocks, ken_blocks):
    naomi_blocks = sorted(naomi_blocks)
    ken_blocks = sorted(ken_blocks)
    result = 0
    while naomi_blocks:
        if naomi_blocks.pop() > ken_blocks[-1]:
            ken_blocks.pop(0)
            result += 1
        else:
            ken_blocks.pop()
    return result


def naomi_deceitful_war_game_score(naomi_blocks, ken_blocks):
    return len(naomi_blocks) - naomi_war_game_score(ken_blocks, naomi_blocks)


def main():
    istream = sys.stdin
    number_of_cases = int(istream.readline())
    for case_no in xrange(1, number_of_cases + 1):
        number_of_blocks = int(istream.readline())
        naomi_blocks = map(float, istream.readline().split())
        ken_blocks = map(float, istream.readline().split())
        assert number_of_blocks == len(naomi_blocks) == len(ken_blocks)
        print 'Case #%d: %d %d' % (case_no,
                                   naomi_deceitful_war_game_score(naomi_blocks, ken_blocks),
                                   naomi_war_game_score(naomi_blocks, ken_blocks))


if __name__ == '__main__':
    main()
