#! /usr/bin/python2.7
# coding: utf-8

# x,r,c<=4

# if x = 1, then gabriel always wins

# x,r,c = 2,1,1 RICHARD
# x,r,c = 2,1,2 GABRIEL
# x,r,c = 2,1,3 RICHARD
# x,r,c = 2,1,4 GABRIEL

## x,r,c = 2,2,1
# x,r,c = 2,2,2 GABRIEL
# x,r,c = 2,2,3 GABRIEL
#   113
#   223
# x,r,c = 2,2,4 GABRIEL

## x,r,c = 2,3,1
## x,r,c = 2,3,2
# x,r,c = 2,3,3 RICHARD
#   123
#   123
#   .44
# x,r,c = 2,3,4 GABRIEL
#   1122
#   3344
#   5566

## x,r,c = 2,4,1
## x,r,c = 2,4,2
## x,r,c = 2,4,3 RICHARD
# x,r,c = 2,4,4 GABRIEL
#   1122
#   3344
#   5566
#   7788


# リチャードが選べるのは2通り .. 両方使って埋められるならガブリエルの必勝
#
# 1.
#
# □□□
#
# 2.
#
# □□
#   □
#

# x,r,c = 3,1,1 RICHARD
# x,r,c = 3,1,2 RICHARD
# x,r,c = 3,1,3 RICHARD; L字を選択すれば埋められないのでリチャードの勝ち
# x,r,c = 3,1,4 RICHARD; L字を選択すれば埋められないのでリチャードの勝ち

## x,r,c = 3,2,1
# x,r,c = 3,2,2 RICHARD
# x,r,c = 3,2,3 GABRIEL
# x,r,c = 3,2,4 RICHARD; I字を選択すれば埋められない
#   1113
#   2223
## x,r,c = 3,3,1
## x,r,c = 3,3,2
# x,r,c = 3,3,3 GABRIEL
#   112
#   122
#   333
# x,r,c = 3,3,4 GABRIEL
#   1113
#   2233
#   2444
## x,r,c = 3,4,1
## x,r,c = 3,4,2
## x,r,c = 3,4,3 RICHARD
# x,r,c = 3,4,4 RICHARD
#   1113
#   2233
#   2444
#   1113


# リチャードが選べるのは5通り
#
# 1.
#   □□□□
#
# 2.
#   □□□
#       □
# 
# 3.
#   □□□
#     □
#
# 4.
#   □□
#     □□
#
# 5.
#   □□
#   □□
#
#

# x,r,c = 4,1,1 RICHARD
# x,r,c = 4,1,2 RICHARD
# x,r,c = 4,1,3 RICHARD
# x,r,c = 4,1,4 RICHARD

## x,r,c = 4,2,1
# x,r,c = 4,2,2 RICHARD
# x,r,c = 4,2,3 RICHARD
# x,r,c = 4,2,4 RICHARD; 3.を指定すると無理
## x,r,c = 4,3,1
## x,r,c = 4,3,2
# x,r,c = 4,3,3 RICHARD; 4.を指定すると無理
# x,r,c = 4,3,4 GABRIEL; どれを指定しても別のを使うと埋められる
## x,r,c = 4,4,1
## x,r,c = 4,4,2
## x,r,c = 4,4,3 RICHARD
# x,r,c = 4,4,4 GABRIEL; どれを指定してもべつのを使うと埋められる

    

result = {
    (1,1,1): 'GABRIEL',
    (1,1,2): 'GABRIEL',
    (1,1,3): 'GABRIEL',
    (1,1,4): 'GABRIEL',

    (1,2,2): 'GABRIEL',
    (1,2,3): 'GABRIEL',
    (1,2,4): 'GABRIEL',

    (1,3,3): 'GABRIEL',
    (1,3,4): 'GABRIEL',

    (1,4,4): 'GABRIEL',

    (2,1,1): 'RICHARD',
    (2,1,2): 'GABRIEL',
    (2,1,3): 'RICHARD',
    (2,1,4): 'GABRIEL',

    (2,2,2): 'GABRIEL',
    (2,2,3): 'GABRIEL',
    (2,2,4): 'GABRIEL',

    (2,3,3): 'RICHARD',
    (2,3,4): 'GABRIEL',

    (2,4,4): 'GABRIEL',

    (3,1,1): 'RICHARD',
    (3,1,2): 'RICHARD',
    (3,1,3): 'RICHARD',
    (3,1,4): 'RICHARD',

    (3,2,2): 'RICHARD',
    (3,2,3): 'GABRIEL',
    (3,2,4): 'RICHARD',

    (3,3,3): 'GABRIEL',
    (3,3,4): 'GABRIEL',

    (3,4,4): 'RICHARD',

    (4,1,1): 'RICHARD',
    (4,1,2): 'RICHARD',
    (4,1,3): 'RICHARD',
    (4,1,4): 'RICHARD',

    (4,2,2): 'RICHARD',
    (4,2,3): 'RICHARD',
    (4,2,4): 'RICHARD',

    (4,3,3): 'RICHARD',
    (4,3,4): 'GABRIEL',

    (4,4,4): 'GABRIEL',
}

for t in xrange(input()):
    x,r,c = map(int, raw_input().split())
    r = result[(x,min(r,c),max(r,c))]
    print 'Case #%d: %s' % (t + 1, r)
