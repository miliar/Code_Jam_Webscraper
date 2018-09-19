import itertools

def solve(sentences):
    seen = {}
    counter = 0
    new_sentences = []
    for sentence in sentences:
        new_sentence = []
        for word in sentence:
            if word not in seen:
                seen[word] = counter
                counter += 1
            new_sentence.append(seen[word])
        new_sentences.append(new_sentence)
    sentences = new_sentences
    e_set_back = set(sentences[0])
    f_set_back = set(sentences[1])
    other_set = set(itertools.chain(*sentences[2:]))
    common_unseen_set = e_set_back.intersection(f_set_back).difference(other_set)
    e_set_back = e_set_back.intersection(other_set)
    f_set_back = f_set_back.intersection(other_set)
    ans = 10000
    for i in xrange(2 ** (len(sentences) - 2)):
        e_list = []
        f_list = []
        for j in xrange(2, len(sentences)):
            if i % 2:
                e_list.append(sentences[j])
            else:
                f_list.append(sentences[j])
            i /= 2
        e_set = e_set_back.union(set(itertools.chain(*e_list)))
        f_set = f_set_back.union(set(itertools.chain(*f_list)))
        #print e_list
        #print f_list
        #print e_set
        #print f_set
        #print e_set.intersection(f_set)
        now = len(e_set.intersection(f_set))
        if now < ans:
            ans = now
    return ans + len(common_unseen_set)

def main():
    T = input()
    for i in xrange(1, T + 1):
        N = input()
        sentences = []
        for j in xrange(N):
            words = raw_input().strip().split()
            sentences.append(words)
        print 'Case #{0}: {1}'.format(i, solve(sentences))


if __name__ == '__main__':
    main()
