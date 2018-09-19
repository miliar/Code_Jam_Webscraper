# make random alphabet
# I didn't know about using the sample when I started, so this is just for
# kicks
import string
import random

test_parameters = ["the quick brown fox jumped over the lazy dog", \
        "your mother was a special one",\
        "i cant believe this works",\
        "still getting over this lousy day",\
        "at least i can concentrate now",\
        "please be quiet in the library",\
        "everyone disable your cell phones now the movie is playing",\
        "just write some random phrase that contains everything"]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_arr = []

def randomize_array(arr, num):
    for i in range(num):
        i = random.randint(0, 25)
        j = random.randint(0, 25)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

random_arr = [i for i in alphabet]
random_arr = randomize_array(random_arr, 200)
beforetrans = "abcdefghijklmnopqrstuvwxyz"
aftertrans = ''.join(random_arr)

trans_table = string.maketrans(beforetrans, aftertrans)

def produce_test_input():
    inputs = []
    for i in range(random.randint(1, 30)):
        inputs.append(test_parameters[i%30])
    f = open("input.txt", 'w')
    f.write(str(len(inputs)))
    for base_string in inputs:
        f.write('\n' + string.translate(base_string, trans_table))
    f.close()

produce_test_input()
