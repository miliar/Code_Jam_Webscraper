#!/usr/bin/env python
import sys

mapping = { 'y' : 'a', # In problem statement
            'e' :'o',
            'q' : 'z'}

TRAINING_SENTENCES = [
                     ("our language is impossible to understand",
                          "ejp mysljylc kd kxveddknmc re jsicpdrysi"),
                     ("there are twenty six factorial possibilities", 
                          "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"),
                     ("so it is okay if you want to just give up",
                          "de kr kd eoya kw aej tysr re ujdr lkgc jv")
                     ]
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def learn_mapping(original_sentence, encoded_sentence):
    for (original, encoded) in zip(original_sentence, encoded_sentence):
        if encoded in mapping: # if we already assigned the mapping, verify it
            if mapping[encoded] != original:
                raise Exception("Mapping mismatch: {0!r} already encoded as {1!r}, but it should be {2!r} as in {3!r}".format(original, mapping[original], encoded, original_sentence))
        else:
            mapping[encoded] = original

def infer_missing_letter() :
    lettercount = 0
    values = set(mapping.values())
    for letter in ALPHABET:
        if letter in mapping:
            continue
        lettercount += 1
        if (lettercount > 1):
            raise Exception("cannot infer {0!r} as more than one letter is missing" \
                                 .format(letter))

        for replacement in ALPHABET:
            if not replacement in values:
                mapping[letter] = replacement
                values.add(replacement)
                break

def encode(original):
    encoded = ""
    for letter in original:
        try:
            encoded += mapping[letter] 
        except KeyError:
            print("Exception when translating {0!r}".format(original))
            raise

    return encoded

if __name__ == '__main__':
    for (original, encoded) in TRAINING_SENTENCES:
        learn_mapping(original, encoded)
    
    infer_missing_letter()

    T = int(sys.stdin.readline())

    for i in range(T):
        s = sys.stdin.readline()
        s = s.replace("\n", "")
        print("Case #{0}: {1}".format(i+1, encode(s)))
        
